if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);
}
 
function count() {
    let counter = localStorage.getItem('counter')
    counter ++;
    document.querySelector('h2').innerHTML = counter;
    localStorage.setItem('counter', counter)
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('h2').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;
});