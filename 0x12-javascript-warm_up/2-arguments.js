#!/usr/bin/node

/*
* Using the argv to check and print based on the number of arguments passed
*/

const args = process.argv;

const argCount = args.lenght - 2;

if (argCount === 0)
{
	console.log('No argument');
}
else if (arCount === 1)
{
	console.log('Argument found');
}
else
{
	console.log('Arguments found');
}
