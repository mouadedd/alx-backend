#!/usr/bin/node
import { createClient, print } from 'redis';

const creat = createClient();

creat.on('connect', () => {
  console.log('Redis client connected to the server');
});

creat.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

creat
  .MULTI()
  .HSET('HolbertonSchools', 'Portland', 50, print)
  .HSET('HolbertonSchools', 'Seattle', 80, print)
  .HSET('HolbertonSchools', 'New York', 20, print)
  .HSET('HolbertonSchools', 'Bogota', 20, print)
  .HSET('HolbertonSchools', 'Cali', 40, print)
  .HSET('HolbertonSchools', 'Paris', 2, print)
  .EXEC();

creat.HGETALL('HolbertonSchools', (err, hashset) => {
  console.log(hashset);
});
