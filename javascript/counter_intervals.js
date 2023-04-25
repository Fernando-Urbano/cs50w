let counter = 0;
 
function count() {
    counter ++;
    document.querySelector('h2').innerHTML = counter;
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = count;

    setInterval(count, 1000);

});