@app.route('/post/attach image/<id>/<postImage>', methods = ['POST', [GET]])
def attach_image(image, post_id):
    if session.get('user_id'):
        if request.method =='POST':
            image = request.form['image']
            post_id = random.randint(100000, 999999)
            post = db.session.query(Note).filter_by(id=post_id).first()
            post = post_id
            user_id = User.query.filter_by(username = username).first()
            username = user.username

            try:

                thisrecord = Posts(post_id, user_id,userName, title,text, image,)
                db.session.add(thisrecord)
                db.session.commit()
                return redirect(url_for('image', username =username, post=id))
            except:

                posts = db.session.query(Note).all()
                print(post)
        else:
            user_one = User_id.query.filter_by(username=username).first()
            post = db.session.query(Note).filter_by(id=post_id).first()
            return render_template('image.html', user_id = user_one, post_id=post)
    else:
        return redirect(url_for('login'))
