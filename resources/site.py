from flask_restful import Resource
from models.site import SiteModel
from flask_jwt_extended import jwt_required

class Sites(Resource):
    def get(self):
        return {'sites': [site.json() for site in SiteModel.query.all()]}

class Site(Resource):
    def get(self, url):
        site = SiteModel.find_site(url)
        if site:
            return site.json()
        return {'message': 'Site not found.'}, 404 # not found

    @jwt_required()
    def post(self, url):
        if SiteModel.find_site(url):
            return {"message": f"The site '{url}' already exists."}, 400 # bad request

        site = SiteModel(url)

        try:
            site.save_site()
        except:
            return {'message': 'An internal error ocurred trying to create a new site.'}, 500 # Internal Server Error

        return site.json()

    @jwt_required()
    def delete(self, url):
        site = SiteModel.find_site(url)
        if site:
            try:
                site.delete_site()
            except:
                return {'message': 'An internal error ocurred trying to delete site.'}, 500 # Internal Server Error

            return {'message': 'Site Deleted.'}

        return {'message': 'site not found'}