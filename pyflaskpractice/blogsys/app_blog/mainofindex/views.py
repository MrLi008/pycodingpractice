# coding=utf8

from flask import render_template, session, redirect, url_for, current_app, flash, request
from flask_login import login_required, current_user

from .. import db

from ..models import User, Role, Post, Permission
from . import mainofindex
from .forms import EditProfileAdminForm, EditProfileForm, PostForm

from ..decorators import admin_required



@mainofindex.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if current_user.can(Permission.WRITE_ARTICLES) \
            and form.validate_on_submit():
        post = Post(body=form.body.data,
                    author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc())\
        .paginate(page,
                  per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                  error_out=False)

    posts = pagination.items

    return render_template('index.html',
                           form=form,
                           posts=posts,
                           pagination=pagination)


@mainofindex.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    pagination = user.posts.order_by(Post.timestamp.desc()).paginate(page,
                                                                     per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                                     error_out=False)
    posts = pagination.items


    return render_template('user.html',
                           user=user,
                           posts=posts,
                           pagination=pagination)


@mainofindex.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data

        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))

    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me

    return render_template('edit_profile.html', form=form)


@mainofindex.route('/edit_profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    print id
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data

        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))

    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me

    return render_template('edit_profile.html', form=form)

# @mainofindex.route('/', methods=['GET', 'POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.name.data).first()
#         if user is None:
#             user = User(username=form.name.data)
#             db.session.add(user)
#             session['known'] = False
#             # if current_app.config['FLASKY_ADMIN']:
#             #     send_email(current_app.config['FLASKY_ADMIN'],
#             #                'New user',
#             #                'mail/new_user',
#             #                user=user)
#             # else:
#             session['known'] = True
#
#             session['name'] = form.name.data
#             return redirect(url_for('index'))
#
#         return render_template('index.html',
#                                form=form,
#                                name=session.get('name'),
#                                known=session.get('known', False))