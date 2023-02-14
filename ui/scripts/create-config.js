const { writeFileSync, existsSync } = require('fs');

const isForceCreate = process.argv[2] === '-f';
const CONFIG_FILE_PATH = './public/config/index.js';

if (!isForceCreate && existsSync(CONFIG_FILE_PATH)) {
  console.log('Config file already exists, doing nothing');
  process.exit();
}

if (!process.env.RECOMMENDATION_API_ENDPOINT) {
  throw new Error('Recommendation API endpoint not defined in enviroment');
}

writeFileSync(
  './public/config/index.js',
  `
export default {
    reviewApi: '${process.env.RECOMMENDATION_API_ENDPOINT}'
};
`
);
