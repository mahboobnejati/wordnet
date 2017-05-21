from flask import request, redirect, url_for, abort, render_template, flash, session
from blog.models import *
from blog.forms import *
import random
from passlib.hash import bcrypt
import itertools
import networkx as nx
import numpy as np
import pandas
import matplotlib.pyplot as plt
import json

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User(username).getUser():
            if bcrypt.verify(password, User(username).getUser().password):
                session['username'] = username
            else:
                error = 'password is not correct.'
        else:
            error = 'there is not any karbar.'
    return render_template('index.html', error=error)


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    flash('Logged out.')
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    error = None
    if request.method == 'POST' and form.validate():
        User(
            username=form.username.data,
            password=bcrypt.encrypt(form.password.data),
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email=form.email.data
        ).addUser()
        return render_template("index.html")

    return render_template('register.html', error=error, form=form)


@app.route('/profile/<username>', methods=['GET'])
def profile(username):
    user = User(username).getUser()
    return render_template('profile.html', user=user)


@app.route('/graph')
def graph():
    return render_template('graph.html')

@app.route('/show_graph')
def show_graph():
    node = NodeInGraph().get_Node()
    source , dest , weight = EdgeInGraph().get_Edge()

    final_source =[]
    final_dest =[]
    final_weight =[]
    final_node =[]

    for itm in source:
        final_source.append(itm[0])
    for itm in dest:
        final_dest.append(itm[0])
    for itm in weight:
        final_weight.append(itm[0])
    for itm in node:
        final_node.append(itm[0])


    list_node = []
    dic_node = {}
    for i in final_node:
        dic_node['name'] = i
        dic_node['group'] = 1
        list_node.append(dic_node.copy())

    list_edge = []
    dic_edge = {}
    for count, item in enumerate(final_source):
        dic_edge['source'] = item
        dic_edge['target'] = final_dest[count]
        dic_edge['weight'] = final_weight[count]
        list_edge.append(dic_edge.copy())

    final_dic = {}
    final_dic['nodes'] = list_node
    final_dic['links'] = list_edge

    graph_file = json.dumps(final_dic, ensure_ascii=False)

    print(graph_file)

    return graph_file

'''
    G = nx.DiGraph()
    for k in node:
        G.add_node

    j=0
    for i in source:
        w = dest[j]
        G.add_edge(i,w)
        j = j+1
'''


    #nx.draw(G)
    #plt.savefig("simple_path.png")  # save as png
    #plt.show()  # display

'''

@app.route('/packfilling/<packId>', methods=['GET', 'POST'])
def packfilling(packId):
    form = ResponseForm(request.form)
    error = None
    if request.method == 'POST' and form.validate():
        #         pack().addResponse(form.response.name, form.response.data,form.response)
        print(form.response.data)

    return render_template('questionnaire.html', error=error, form=form, stimulus=stimulus)
'''


