$(function () {
    if (window.location.hash) {
        hash = window.location.hash;
        console.log('hash: ' + hash);
        if (hash.includes('#date')) {
            console.log($('h1').text());
            $('h1').text('' + Math.random());
        }
    } else {
        console.log('no hash');
    }
});
