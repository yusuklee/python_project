from flask import Flask, render_template, request
import asyncio
from exchange import convert_and_get_rates, generate_chart

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    result= None
    chart = None

    if request.method =='POST':
        base=request.form.get('base').strip().upper() 
        amount = float(request.form.get('amount'))
        targets = [t.strip().upper() for t in request.form.get('targets').split(',')]

        loop = asyncio.new_event_loop() #flask에서 비동기함수 실행하려면 이렇게함.
        asyncio.set_event_loop(loop)  
        result = loop.run_until_complete(convert_and_get_rates(base, targets, amount))

        chart = generate_chart(base, result)

    return render_template('index.html', result=result,chart=chart) #사용할 html과 그 html에 넘겨줄값


if __name__== '__main__':
    app.run(debug=True)
    