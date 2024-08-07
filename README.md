# HNM Clothing Store
![Screenshot 2024-08-04 at 6 04 45 PM](https://github.com/user-attachments/assets/e65c5b0a-ca78-4de7-9938-ee02c604506f)

## Tech Stack 🧰
-   HTML
-   CSS
-   JavaScript
-   Bootstrap
-   Python
-   Flask
-   SQLAlchemy
-   SQLite
-   Monolith Architecture (users <=> frontend & backend <=> database)

## Views 🧐
### What a curious user who is not signed in would see:<be>
![Screenshot 2024-08-04 at 6 45 12 PM](https://github.com/user-attachments/assets/3d012c51-fc1e-46cb-8bdd-7420bf7481c4)
![Screenshot 2024-08-04 at 6 45 21 PM](https://github.com/user-attachments/assets/dfcad3ab-82fa-43b8-bd82-4e3ccf0973e4)

### Sign Up or Log In:
![Screenshot 2024-08-04 at 6 46 54 PM](https://github.com/user-attachments/assets/8e15c0f5-e1f3-4787-a376-5e5c86bd8407)
![Screenshot 2024-08-04 at 6 47 03 PM](https://github.com/user-attachments/assets/08df6b4d-575e-466e-b516-6a439eb4a5ad)

### Logged in as owner:<be>
![Screenshot 2024-08-04 at 6 05 17 PM](https://github.com/user-attachments/assets/7d6aa0c1-1eb6-4233-9017-a72fa732ce8a)
![Screenshot 2024-08-04 at 6 05 08 PM](https://github.com/user-attachments/assets/fce5a975-c2a0-4de7-b25e-26a745bd951f)
![Screenshot 2024-08-04 at 6 05 28 PM](https://github.com/user-attachments/assets/f5f64c06-86cb-4513-8842-c44db90dc1bf)

### Logged in as customer:<br>
![Screenshot 2024-08-04 at 6 05 37 PM](https://github.com/user-attachments/assets/613cb50b-56a0-47fa-ba78-7dde436e42e4)
![Screenshot 2024-08-04 at 6 06 09 PM](https://github.com/user-attachments/assets/0b3613cc-3f8d-4997-af97-3420e01cc6d8)
![Screenshot 2024-08-04 at 6 06 25 PM](https://github.com/user-attachments/assets/9f7d1d71-d2bb-4249-b29c-cf631c1289c9)
![Screenshot 2024-08-04 at 6 51 33 PM](https://github.com/user-attachments/assets/4f7c4eeb-3dc1-4b16-b6f6-1aa3491c7d75)


## Functionalities 📋
There are two types of users, **Owner** and **Customer**.

**Owner** actions:
- Sign in/out
- Add items 
- Edit items info
- Delete items

**Customer** actions:
- Sign in/out
- Add to cart
- View cart
- Remove items from their cart
- Submit an order
- Edit their billing information

**Note: If a user visits the website and is not signed in as either an Owner/Customer, then they will only be able to view the items. To do more, they most sign up for an account or log into an existing account.**

## Database 📀
- Enhanced Entity-Relationship Modelling
  ![Screenshot 2024-08-04 at 6 57 06 PM](https://github.com/user-attachments/assets/43608a2e-7099-4263-8c83-b7c445bd8be0)
- Final implementation in SQLite<br/>
  ![Screenshot 2024-08-04 at 6 54 40 PM](https://github.com/user-attachments/assets/3e6383ce-0bf2-485d-97e1-93f9b7acfdfc)

### Some Queries Examples 🔎
SQLAlchemy Method | SQL Equivalent |
--- | --- | 
items = Item.query.all() | SELECT * FROM item  |
User.query.get(int(user_id)) | SELECT * FROM  user WHERE (id=user_id)  |
User.query.filter_by(email_address=sign_up_form.email.data).first(): | SELECT * FROM  user WHERE (email_address=sign_up_form_email.data) LIMIT 1;  |
db.session.delete(item_to_delete) | DELETE FROM item WHERE (id=item_id) LIMIT 1;  |
new_order = Order(order_date=current_data_time.strftime("%d/%m/%Y %H:%M:%S"), total_price=0,user_id=customer_user.id) db.session.add(new_order) | INSERT INTO order (order_date, total_price, user_id) VALUES (current_data_time.strftime(“%d/%m/%Y %H:%M:%S”), 0, customer_user.id);  |
item_inventory_id = item_row.inventory_id old_inventory_row = Inventory.query.filter_by(id=item_inventory_id).first() old_inventory_row.stock = old_inventory_row.stock + 1 | UPDATE inventory SET stock = (stock + 1) WHERE (SELECT * FROM inventory WHERE (id=item_inventory_id) LIMIT 1);  |

 












