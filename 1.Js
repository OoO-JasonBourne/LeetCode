var callbacks = []
for (var i = 0; i < 4; i++) {
callbacks.push(function() {
console.log(i);
});
}
callbacks.forEach(cb => cb());