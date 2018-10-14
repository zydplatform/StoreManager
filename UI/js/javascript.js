var login = document.getElementById('login');

login.addEventListener('submit', function(e){
    e.preventDefault();
    if (e.target.username.value == 'admin' && e.target.password.value == 'admin'){
        e.target.username.value = '';
        e.target.username.value = '';
        window.location.href = 'admin/all_sales.html'
    } else if (e.target.username.value == 'attendant' && e.target.password.value == 'attendant'){
        e.target.username.value = '';
        e.target.username.value = '';
        window.location.href = 'attendant/sell_product.html';
    }
});