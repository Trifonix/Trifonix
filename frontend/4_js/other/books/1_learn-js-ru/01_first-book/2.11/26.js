if (-1 || 0) console.log("first"); // -1 -> true
if (-1 && 0) console.log("second"); // 0 -> false
if (null || (-1 && 1)) console.log("third"); // 1 -> true
