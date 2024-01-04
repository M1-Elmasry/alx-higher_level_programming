#!/usr/bin/node

const request = require('request');

const baseUrl = process.argv[2];

request.get(baseUrl, undefined, (err, _res, body) => {
  if (err) console.log(err);
  else {
    const todos = JSON.parse(body);
    const completedTodosByUser = {};
    for (const todo of todos) {
      if (todo.completed) {
        completedTodosByUser[todo.userId]
          ? completedTodosByUser[todo.userId]++
          : completedTodosByUser[todo.userId] = 1;
      }
    }
    console.log(completedTodosByUser);
  }
});
