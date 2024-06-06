var width = 0;
var interval = setInterval(frame, 50); // 5000 ms / 100 = 50 ms
function frame() {
    if (width >= 100) {
        clearInterval(interval);
    } else {
        width++;
        document.getElementById('progressBar').firstElementChild.style.width = width + '%';
    }
}