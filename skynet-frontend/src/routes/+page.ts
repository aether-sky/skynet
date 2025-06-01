// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
//export const prerender = true;
export const prerender = false;
import type { PageLoad } from './$types';
import { API_BASE_URL } from "$lib/constants";

export const load: PageLoad = async () => {
  const res = await fetch(API_BASE_URL + '/items/123');
  const posts: { item_id: number; q: string }[] = await res.json();

  return {
    posts
  };
};