from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from grocery_app.models import GroceryStore, GroceryItem
from grocery_app.forms import GroceryStoreForm, GroceryItemForm

# Import app and db from events_app package so that we can run app
from grocery_app.extensions import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    all_stores = GroceryStore.query.all()
    print(all_stores)
    return render_template('home.html', all_stores=all_stores)

@main.route('/new_store', methods=['GET', 'POST'])
def new_store():
    #  Create a GroceryStoreForm
    form = GroceryStoreForm()
    
    if form.validate_on_submit():
        store = GroceryStore(
            title=form.title.data,
            address=form.address.data
        )
        db.session.add(store)
        db.session.commit()
        # - flash a success message, and
    # - redirect the user to the store detail page.

        flash('Store Created.')
        return redirect(url_for('main.store_detail', store_id=store.id))
    
    # Send the form to the template and use it to render the form fields
    return render_template('new_store.html', form=form)

@main.route('/new_item', methods=['GET', 'POST'])
def new_item():
    form = GroceryItemForm()
    #  If form was submitted and was valid:
    # - create a new GroceryItem object and save it to the database,
    # - flash a success message, and
    # - redirect the user to the item detail page.

    if form.validate_on_submit():
        item = GroceryItem(
            name=form.name.data,
            price=form.price.data,
            category=form.category.data,
            photo_url=form.photo_url.data,
            store=form.store.data
        )
        db.session.add(item)
        db.session.commit()
            # - flash a success message, and
        # - redirect the user to the store detail page.

        flash('Item added.')
        return redirect(url_for('main.store_detail', store_id=item.store.id))

    # : Send the form to the template and use it to render the form fields
    else:
        return render_template('new_item.html', form=form)


@main.route('/store/<store_id>', methods=['GET', 'POST'])
def store_detail(store_id):
    # Create a GroceryItemForm

    store = GroceryStore.query.get(store_id)
    form = GroceryStoreForm(obj=store)

    #  If form was submitted and was valid:
    # - create a new GroceryItem object and save it to the database,
    # - flash a success message, and
    # - redirect the user to the item detail page.

    if form.validate_on_submit():
        store.title = form.title.data
        store.address = form.address.data
        db.session.add(store)
        db.session.commit()
        # - flash a success message, and
    # - redirect the user to the store detail page.

        flash('Store Updated.')
        return redirect(url_for('main.store_detail', store_id=store.id))

    # Send the form to the template and use it to render the form fields
    return render_template('store_detail.html', form=form, store=store)

@main.route('/item/<item_id>', methods=['GET', 'POST'])
def item_detail(item_id):
    item = GroceryItem.query.get(item_id)
    # Create a GroceryItemForm and pass in `obj=item`
    form = GroceryItemForm(obj=item)
    #  If form was submitted and was valid:
    # - update the GroceryItem object and save it to the database,
    # - flash a success message, and
    # - redirect the user to the item detail page.

    if form.validate_on_submit():
        item.name = form.name.data
        item.price = form.price.data
        item.category = form.category.data
        item.photo_url = form.photo_url.data
        item.store = form.store.data
        # - flash a success message, and
    # - redirect the user to the store detail page.
        db.session.add(item)
        db.session.commit()
        flash('item Updated.')
        print('updated!')
        return redirect(url_for('main.item_detail', item_id=item.id))

    # Send the form to the template and use it to render the form fields
    
    return render_template('item_detail.html', item=item, form=form)

