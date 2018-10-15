var login = document.getElementById('login');
var wrongUsername = document.getElementById('wrong-username');
var wrongPassword = document.getElementById('wrong-password');


login.addEventListener('submit', function(e){
    e.preventDefault();

    if (e.target.username.value == 'admin' && e.target.password.value == 'admin'){
        window.location.href = 'admin/all_sales.html';
    } else if (e.target.username.value == 'attendant' && e.target.password.value == 'attendant'){
        window.location.href = 'attendant/sell_product.html';
    }

    if (e.target.username.value == ''){
        wrongUsername.style.display = 'block';
        wrongUsername.innerText = 'Provide Username';
    }else if (e.target.username.value != 'admin' || e.target.username.value != 'attendant'){
        wrongUsername.style.display = 'block';
        wrongUsername.innerText = 'wrong username';
    }

    if (e.target.password.value == ''){
        wrongPassword.style.display = 'block';
        wrongPassword.innerText = 'Provide Password';
    }else if (e.target.password.value != 'admin' || e.target.password.value != 'attendant'){
        wrongPassword.style.display = 'block';
        wrongPassword.innerText = 'wrong password';
    }

   
});