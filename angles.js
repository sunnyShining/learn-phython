let a = [1];
for (let i = 0; i <= 10; i++) {
	console.log(a);
	a[i + 1] = 0;
	b = [...a];
	for (let j = 0; j <= i + 1; j++) {
		if (j == 0) {
			a[j] = 1;
		} else {
			a[j] = b[j - 1] + b[j];
		}
	}
}