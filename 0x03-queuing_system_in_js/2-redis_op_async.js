#!/usr/bin/node

import { promisify } from 'util';
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

async function displaySchoolValue(schoolName) {
  const GET = promisify(creat.GET).bind(creat);
  try {
    const value = await GET(schoolName);
    console.log(value);
  } catch (error) {
    console.log(error.toString());
  }
}

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
