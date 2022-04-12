from flask import render_template,Flask,request
import pickle

app=Flask(__name__)
file=open("dt_pipeline.pkl","rb")
decision_tree=pickle.load(file)
file.close()

@app.route("/", methods=["GET","POST"])
def home():
    if request.method=="POST":
        myDict = request.form
        N = float(myDict["N"])
        P = float(myDict["P"])
        K=float(myDict["K"])
        PH = float(myDict["PH"])
        EC = float(myDict["EC"])
        S = float(myDict["S"])
        Cu = float(myDict["Cu"])
        Fe = float(myDict["Fe"])
        Mn = float(myDict["Mn"])
        Zn = float(myDict["Zn"])
        B = float(myDict["B"])
        
        pred = [N,P,K,PH,EC,S,Cu,Fe,Mn,Zn,B]
        Crop_Pred=decision_tree.predict([pred])[0]
        Confidence = round(max(decision_tree.predict_proba([pred])[0])*100,2)
        print(Confidence)
        if(Crop_Pred==0):
            res="Grapes"
        if(Crop_Pred==1):
            res="Mango"
        if(Crop_Pred==2):
            res="Mulberry"
        if(Crop_Pred==3):
            res="Pomegranate"
        if(Crop_Pred==4):
            res="Potato"
        if(Crop_Pred==5):
            res="Ragi"
        return render_template('result.html',N=N,P=P,K=K,PH=PH,
        EC=EC,S=S,Cu=Cu,Fe=Fe,Mn=Mn,Zn=Zn,B=B,res=res,conf=Confidence)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)
