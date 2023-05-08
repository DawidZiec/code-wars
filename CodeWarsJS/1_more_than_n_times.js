function deleteNth(arr, n) {
  let result = [];
  let current_values = [];
  for (let t = 0; t < n; t++) {
    for (let i = 0; i < arr.length; i++) {
      if (current_values.includes(arr[i]) == false) {
        current_values.push(arr[i]);
        result.push(arr[i]);
      }
    }
    current_values = [];
  }
  return result;
}
