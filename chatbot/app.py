from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def search_product_by_name_or_description(term):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    query = "SELECT * FROM products WHERE name LIKE ? OR description LIKE ?"
    cursor.execute(query, ('%' + term + '%', '%' + term + '%'))
    products = cursor.fetchall()

    conn.close()
    return products

@app.route('/search', methods=['GET'])
def search():
    search_term = request.args.get('term', '').strip().lower()

    if not search_term:
        return jsonify({'error': 'Search term not provided'})

    results = search_product_by_name_or_description(search_term)
    
    greeting_message = "Claro, aqui esta o que você procura:"

    if results:
        products_list = [{'name': product[1], 'description': product[2]} for product in results]
        return jsonify({
            'greeting': greeting_message,
            'products': products_list,
        })
    else:
        return jsonify({'message': 'Desculpe, eu não encontrei o que você esta procurando :('})

if __name__ == "__main__":
    app.run(debug=True)