#!/usr/bin/node

import { createClient } from 'redis';

const creat = createClient();

creat.on('connect', () => {
  console.log('Redis client connected to the server');
});

creat.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});
