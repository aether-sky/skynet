// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
//export const prerender = true;
export const prerender = false;
import type { PageLoad } from './$types';
import { API_BASE_URL } from '$lib/constants';

export const load: PageLoad = async () => {
  const fetchData = async (url: string): Promise<any> => {
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    } catch (error) {
      console.error('Fetch error:', error);
      return { error: 'Failed to fetch data' };
    }
  };
  const url = API_BASE_URL + '/items/123';
  const posts: { item_id: number; q: string }[] = await fetchData(url);
  const models: { id: string; name: string }[] = [
    { id: '1', name: 'Simple (Llama 3 8B)' },
    { id: '2', name: 'Unhelpful (Llama 3 8B)' },
    { id: '3', name: 'Custom trained (Llama 3 8B)' },
  ]; //await fetchData(modelsUrl);

  return {
    posts,
    models,
  };
};
