#!/usr/bin/node

import { createClient, print } from 'redis';

const creat = createClient();

creat.on('connect', () => {
  console.log('Redis client connected to the server');
});

creat.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

function setNewSchool(schoolName, value) {
  creat.SET(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  creat.GET(schoolName, (err, value) => {
    console.log(value);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
