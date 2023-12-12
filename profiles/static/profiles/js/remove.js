// Remove footer and background img
const footer = document.querySelector('footer.container-fluid.bg-dark.text-white.py-1');
if (footer) {
    footer.remove();
    document.body.style.backgroundImage = 'none';
}