#!/usr/bin/node
const args = process.argv;
if (args.length === 2) {
	let none = "No argument"
	console.log(none)
} else if (args.length === 3){
	let yes = "Argument found";
	console.log(yes)
} else {
	let fin = "Arguments found";
	console.log(fin);
}
