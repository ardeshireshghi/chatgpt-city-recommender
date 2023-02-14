import config from '/config/index.js';

function createRequest({ url, method, data }) {
  const options = {
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
    method,
  };

  return {
    async send() {
      const rawResponse = await fetch(url, options);
      if (!rawResponse.ok) {
        throw new Error('Invalid request response');
      }

      const parsedResponse = await rawResponse.json();
      return parsedResponse;
    },
  };
}

export async function getRecommandations({ city, interests } = {}) {
  const apiRequest = createRequest({
    url: config.reviewApi,
    data: {
      city,
      interests,
    },
    method: 'POST',
  });

  const parsedResponse = await apiRequest.send();
  return parsedResponse.data.recommendations;
}
