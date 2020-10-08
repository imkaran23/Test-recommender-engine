import pandas as pd
import pickle
from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, jsonify, request
import traceback
import json

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def home():
    return "<h1>RECOMMENDER ENGINE</h1><p>This is a prototype API for recommending products for an user.</p>"

# parser = reqparse.RequestParser()
# parser.add_argument('user_id', type=str, help="USER ID", required=True)
# parser.add_argument('category', type=str, help="CATEGORY", required=False, default=None)
# # if 'rating' in args: pass

# class Predict(Resource):        
#     def post(self):
#         try: 
#             args = parser.parse_args(strict=True)
#             user_id = args['user_id']
#             users, items, preds = [], [], []
#             data = pd.read_csv('../Post dataset/data.csv')
#             item = list(data.itemID.unique())
#             for user in user_id:
#                 user = [user] * len(item)
#                 users.extend(user)
#                 items.extend(item)

#             all_predictions = pd.DataFrame(data={"userID": users, "itemID": items})
#             all_predictions["uid"] = all_predictions.userID.map(uid_map)
#             all_predictions["iid"] = all_predictions.itemID.map(iid_map)


#             dok_weights = interactions.todok()
#             all_predictions["rating"] = all_predictions.apply(
#                 lambda x: dok_weights[x.uid, x.iid], axis=1
#             )

#             all_predictions = all_predictions[all_predictions.rating < 1].reset_index(drop=True)
#             all_predictions = all_predictions.drop("rating", axis=1)

#             all_predictions["prediction"] = all_predictions.apply(
#                 lambda x: model.predict(
#                     user_ids=x["uid"],
#                     item_ids=[x["iid"]],
#                     user_features=user_features,
#                     item_features=item_features,
#                     num_threads=num_threads,
#                 )[0],
#                 axis=1,
#             )

#             all_predictions['prediction'] = all_predictions.apply(lambda x: -x['prediction'],axis=1)
#             all_predictions.sort_values(by=['prediction'],inplace=True)
#             all_predictions = all_predictions[["userID", "itemID", "prediction"]]
#             responses = all_predictions.to_json(orient="records")

#             return responses,200
        
#         except:
#             return jsonify({'trace': traceback.format_exc()})

# api.add_resource(Predict, '/predict')

@app.route('/predict', methods=['POST'])
def predict_by_userID():
    try:
        user_id = request.json
        return jsonify({'ID':user_id}),200
        users, items, preds = [], [], []
        data = pd.read_csv('Post dataset/data.csv')
        item = list(data.itemID.unique())
        for user in user_id:
            user = [user] * len(item)
            users.extend(user)
            items.extend(item)
        
        all_predictions = pd.DataFrame(data={"userID": users, "itemID": items})
        all_predictions["uid"] = all_predictions.userID.map(uid_map)
        all_predictions["iid"] = all_predictions.itemID.map(iid_map)
        
        
        dok_weights = interactions.todok()
        all_predictions["rating"] = all_predictions.apply(
            lambda x: dok_weights[x.uid, x.iid], axis=1
        )

        all_predictions = all_predictions[all_predictions.rating < 1].reset_index(drop=True)
        all_predictions = all_predictions.drop("rating", axis=1)

        all_predictions["prediction"] = all_predictions.apply(
            lambda x: model.predict(
                user_ids=x["uid"],
                item_ids=[x["iid"]],
                user_features=user_features,
                item_features=item_features,
                num_threads=num_threads,
            )[0],
            axis=1,
        )

        all_predictions['prediction'] = all_predictions.apply(lambda x: -x['prediction'],axis=1)
        all_predictions.sort_values(by=['prediction'],inplace=True)
        all_predictions = all_predictions[["userID", "itemID", "prediction"]]
        responses = all_predictions.to_json(orient="records")
        
        return responses,200
    
    except:
        return jsonify({'trace': traceback.format_exc()})

if __name__ =="__main__":
    model = open("model2.pickle","rb")
    model = pickle.load(model)

    uid_map = open("uid_map.pickle","rb")
    uid_map = pickle.load(uid_map)

    iid_map = open("iid_map.pickle","rb")
    iid_map = pickle.load(iid_map)

    interactions = open("train_interactions2.pickle","rb")
    interactions = pickle.load(interactions)

    user_features = open("user_features.pickle","rb")
    user_features = pickle.load(user_features)

    item_features = open("item_features.pickle","rb")
    item_features = pickle.load(item_features)
    
    num_threads = 8    
    app.run(debug=True)
