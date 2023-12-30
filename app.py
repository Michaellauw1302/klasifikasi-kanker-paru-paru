from flask import Flask, render_template, request, redirect
import sklearn
import pickle

app = Flask(__name__)

model = pickle.load(open('modelRF.pkl', 'rb'))
#
# @app.route('/')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # jk = float(request.form['jk'])
        # umur = float(request.form['umur'])
        # rokok = float(request.form['rokok'])
        # jari = float(request.form['jari'])
        # peer = float(request.form['peer'])
        # kronis = float(request.form['kronis'])
        # fatigue = float(request.form['fatigue'])
        # alergi = float(request.form['alergi'])
        # nafas = float(request.form['nafas'])

        # alkohol = float(request.form['alkohol'])
        # batuk = float(request.form['batuk'])
        # sesak = float(request.form['sesak'])
        # susah_telan = float(request.form['susah_telan'])
        # dada = float(request.form['dada'])
        # datas = np.array([jk, umur, rokok, jari, peer, kronis,
        #                   fatigue, alergi, nafas, alkohol, batuk, sesak, susah_telan, dada])
        # datas = np.reshape(datas, (1, -1))
        # isKanker = model.predict(datas)
        jk, umur, rokok, jari, anxiety, peer, kronis, fatigue, alergi, nafas, alkohol, batuk, sesak, susah_telan, dada = [
            x for x in request.form.values()]
        data = []

        data.append(int(jk))
        data.append(int(umur))
        data.append(int(rokok))
        data.append(int(jari))
        data.append(int(anxiety))
        data.append(int(peer))
        data.append(int(kronis))
        data.append(int(fatigue))
        data.append(int(alergi))
        data.append(int(nafas))
        data.append(int(alkohol))
        data.append(int(batuk))
        data.append(int(sesak))
        data.append(int(susah_telan))
        data.append(int(dada))
        # data.append(int(dada))
        # print("boom")
        prediction = model.predict([data])

        # return render_template('hasil.html', Status=prediction, jk=jk, umur=umur, rokok=rokok, jari=jari, peer=peer, kronis=kronis, fatigue=fatigue, alergi=alergi, nafas=nafas, alkohol=alkohol, batuk=batuk, sesak=sesak, susah_telan=susah_telan, dada=dada)
        return render_template('hasil.html', Status=prediction)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
