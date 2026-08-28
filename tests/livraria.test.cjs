const assert = require('node:assert/strict');
const test = require('node:test');

test('lista os tres livros do catalogo', async () => {
    const response = await fetch('http://localhost:3000/products');
    assert.equal(response.status, 200);
    const products = await response.json();
    assert.deepEqual(products.map((product) => product.id), [1, 2, 3]);
});

for (const [id, name] of [[1, 'Refactoring'], [2, 'Engenharia De Software Moderna'], [3, 'Design Patterns']]) {
    test(`busca o livro ${id} pelo identificador`, async () => {
        const response = await fetch(`http://localhost:3000/product/${id}`);
        assert.equal(response.status, 200);
        const product = await response.json();
        assert.equal(product.id, id);
        assert.equal(product.name, name);
    });
}

test('consulta o frete pelo controller', async () => {
    const response = await fetch('http://localhost:3000/shipping/85810000');
    assert.equal(response.status, 200);
    const shipping = await response.json();
    assert.equal(shipping.cep, '85810000');
    assert.equal(typeof shipping.value, 'number');
    assert.ok(shipping.value >= 1 && shipping.value <= 101);
});
