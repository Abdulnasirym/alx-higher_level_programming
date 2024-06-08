#!/usr/bin/node
const args = process.argv;
if (args.length === 2) {
	const none = "No argument"
	console.log(none)
} else if (args.length === 3){
	const yes = "Argument found";
	console.log(yes)
} else {
	const fin = "Arguments found";
	console.log(fin);
}
