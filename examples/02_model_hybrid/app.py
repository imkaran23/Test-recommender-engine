import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

if __name__ =="__main__":
    app.run()

# import pandas as pd
# import pickle
# from flask_restful import reqparse, abort, Api, Resource
# from flask import Flask, jsonify, request

# app = Flask(__name__)
# app.config["DEBUG"] = True
# # api = Api(app)

# # print("Loading the model and other files...")
# # model2_copy = open("model2.pickle","rb")
# # model2_copy = pickle.load(model2_copy)

# # uid_map = open("uid_map.pickle","rb")
# # uid_map = pickle.load(uid_map)

# # iid_map = open("iid_map.pickle","rb")
# # iid_map = pickle.load(iid_map)

# # train_interactions2 = open("train_interactions2.pickle","rb")
# # train_interactions2 = pickle.load(train_interactions2)

# # user_features = open("user_features.pickle","rb")
# # user_features = pickle.load(user_features)

# # item_features = open("item_features.pickle","rb")
# # item_features = pickle.load(item_features)
# # print("The model and files has been loaded...doing predictions now...")

# # parser = reqparse.RequestParser()
# # parser.add_argument('user_id')

# # class Predict(Resource):        
# #     def sample_recommendation(
# # #         user_id,
# #         data,
# #         uid_map,
# #         iid_map,
# #         interactions,
# #         model,
# #         num_threads,
# #         user_features=None,
# #         item_features=None,
# #     ):
# #         args = parser.parse_args()
# #         user_id = args['user_id']
        
# #         users, items, preds = [], [], []
# #         item = list(data.itemID.unique())
# #         for user in user_id:
# #             user = [user] * len(item)
# #             users.extend(user)
# #             items.extend(item)

# #         all_predictions = pd.DataFrame(data={"userID": users, "itemID": items})
# #         all_predictions["uid"] = all_predictions.userID.map(uid_map)
# #         all_predictions["iid"] = all_predictions.itemID.map(iid_map)

# #         dok_weights = interactions.todok()
# #         all_predictions["rating"] = all_predictions.apply(
# #             lambda x: dok_weights[x.uid, x.iid], axis=1
# #         )

# #         all_predictions = all_predictions[all_predictions.rating < 1].reset_index(drop=True)
# #         all_predictions = all_predictions.drop("rating", axis=1)

# #         all_predictions["prediction"] = all_predictions.apply(
# #             lambda x: model.predict(
# #                 user_ids=x["uid"],
# #                 item_ids=[x["iid"]],
# #                 user_features=user_features,
# #                 item_features=item_features,
# #                 num_threads=num_threads,
# #             )[0],
# #             axis=1,
# #         )

# #         all_predictions['prediction'] = all_predictions.apply(lambda x: -x['prediction'],axis=1)
# #         all_predictions.sort_values(by=['prediction'],inplace=True)
# #         all_predictions = all_predictions[["userID", "itemID", "prediction"]]
# #         responses = jsonify(predictions=all_predictions.to_json(orient="records"))
# #         return responses

    
# # api.add_resource(Predict, '/')

# # if __name__ =="__main__":
# #     app.run(debug=True)