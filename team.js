let array = [3, -1, -5, 2, 5, -9, 0];
let array2 = [-10, -2, 0];

let mul = 1;

for (let i of array) {
  mul = mul * i;
}

/*

i have to check the cases
first if the multiplication is zero
stay focused

return the array excluding 0

how to use reduce function in js 

*/

if (mul === 0) {
  let newArray = [];
  for (let i of array) {
    if (i == 0) {
      continue;
    } else {
      newArray.push(i);
    }
  }
  console.log(newArray.reduce((total, cv, i) => total * cv));
  console.log(newArray);
  let mul = 1;
  for (let i of newArray) {
    mul = mul * i;
  }
  if (mul > 0) {
    newArray.sort();
    console.log(newArray.join(" "));
  } else {
    console.log(mul);
  }
} else if (mul > 1) {
  console.log("ff");
}
