from flask_restful import Resource, reqparse;
from models.user import UserModel;

class UserRegister(Resource):
    parser = reqparse.RequestParser();
    parser.add_argument(
                        'username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
    );
    parser.add_argument(
                        'password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
    );
    def post(self):
        #get request data
        data = UserRegister.parser.parse_args();

        #check user already exist or not
        if UserModel.find_by_username(data['username']):
            return {'message' : 'User name {} already exist'.format(data['username'])}, 400;

        user = UserModel(data['username'], data['password']);
        user.save_to_db();
        #return the success message
        return {'Message':'User register successfully'}, 201
