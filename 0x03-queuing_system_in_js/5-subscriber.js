#!/usr/bin/node

import { createClient } from 'redis';

const creat = createClient();


creat.on('connect', () => {
  console.log('Redis client connected to the server');
});

creat.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const even = (message) => console.log(message);

creat.SUBSCRIBE('holberton school channel');

creat.on('message', (channel, message) => {
  if (channel === 'holberton school channel') {
    if (message === 'KILL_SERVER') {
      creat.UNSUBSCRIBE();
      creat.QUIT();
    }
    even(message);
  }
});
