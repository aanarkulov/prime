/**
 * Copyright 2016 Google Inc. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

// DO NOT EDIT THIS GENERATED OUTPUT DIRECTLY!
// This file should be overwritten as part of your build process.
// If you need to extend the behavior of the generated service worker, the best approach is to write
// additional code and include it using the importScripts option:
//   https://github.com/GoogleChrome/sw-precache#importscripts-arraystring
//
// Alternatively, it's possible to make changes to the underlying template file and then use that as the
// new base for generating output, via the templateFilePath option:
//   https://github.com/GoogleChrome/sw-precache#templatefilepath-string
//
// If you go that route, make sure that whenever you update your sw-precache dependency, you reconcile any
// changes made to this original template file with your modified copy.

// This generated service worker JavaScript will precache your site's resources.
// The code needs to be saved in a .js file at the top-level of your site, and registered
// from your pages in order to be used. See
// https://github.com/googlechrome/sw-precache/blob/master/demo/app/js/service-worker-registration.js
// for an example of how you can register this script and handle various service worker events.

/* eslint-env worker, serviceworker */
/* eslint-disable indent, no-unused-vars, no-multiple-empty-lines, max-nested-callbacks, space-before-function-paren, quotes, comma-spacing */
'use strict';

var precacheConfig = [["/about-us.html","806b8c198738c56cfbbd1a22aedc7130"],["/contacts.html","b633006c0192852e8dcaf4ea59bae18d"],["/css/libs.min.css","527b944bf54766dee851c27ebc0119e2"],["/css/style.min.css","0ca23b1565e7694d29460bc5a33ad547"],["/diagnostic-inner.html","f4bfc3c34d5454ec5fa6b77d8ee05f31"],["/diagnostics-inner.html","80ec2c2a53d94d16a9998325766f44bf"],["/diagnostics.html","433d257a5f2863d0bb121792cc833bc6"],["/doctor.html","e55692e0b01990bc460c080ad33930da"],["/doctors.html","9d88f16a28af27e099cd25881a2c6218"],["/enter.html","665dbc893bfbdad1778a06fd1dff35e7"],["/faq.html","a2ea2157af65584b630e61cff7676378"],["/fonts/FontAwesome.otf","0d2717cd5d853e5c765ca032dfd41a4d"],["/fonts/OpenSansBold/OpenSansBold.eot","08862c283f9f67a94116085cc5ba989d"],["/fonts/OpenSansBold/OpenSansBold.ttf","c3b34d59ef4c949d25a4f32b5096471a"],["/fonts/OpenSansBold/OpenSansBold.woff","eff2996162fdfe7c6af7995d3f790275"],["/fonts/OpenSansLight/OpenSansLight.eot","eb578c83a7d79f561b41d2436c5a9f35"],["/fonts/OpenSansLight/OpenSansLight.ttf","12c8a8c628ce99ed729f003698183a3a"],["/fonts/OpenSansLight/OpenSansLight.woff","f5e96f06811c03c019d10f2a8402303a"],["/fonts/OpenSansRegular/OpenSansRegular.eot","91e049db2f1148f1f0e607bfbcba1a47"],["/fonts/OpenSansRegular/OpenSansRegular.ttf","5874364d5ae80a8671d620d78ff9f1b5"],["/fonts/OpenSansRegular/OpenSansRegular.woff","0f7c77932ea877aca544e439a3e63bb6"],["/fonts/fontawesome-webfont.eot","674f50d287a8c48dc19ba404d20fe713"],["/fonts/fontawesome-webfont.svg","acf3dcb7ff752b5296ca23ba2c7c2606"],["/fonts/fontawesome-webfont.ttf","b06871f281fee6b241d60582ae9369b9"],["/fonts/fontawesome-webfont.woff","fee66e712a8a08eef5805a46892932ad"],["/fonts/fontawesome-webfont.woff2","af7ae505a9eed503f8b8e6982036873e"],["/fonts/lg.eot","ecff11700aad0000cf3503f537d1df17"],["/fonts/lg.svg","98d62b1e5f5b556facf319b19c6c7cba"],["/fonts/lg.ttf","4fe6f9caff8b287170d51d3d71d5e5c6"],["/fonts/lg.woff","5fd4c338c1a1b1eeeb2c7b0a0967773d"],["/img/jpg/advantages.jpg","d5eba5f78448c76055e0e2635926e795"],["/img/jpg/bgbr.jpg","1493a106447c04ef034cd602893cf53b"],["/img/jpg/dia0.jpg","3850dc89b99d8972d76915e2a6bb6cae"],["/img/jpg/diag.jpg","8dd350eba5491e698b09fe4b1f005d01"],["/img/jpg/doctor.jpg","f5ce98a7900dc65c664c1f8a0deedf01"],["/img/jpg/garant.jpg","0306f26e00588d31d17a3cabd560c170"],["/img/jpg/modal.jpg","33ae5b355aabb15b7114f8c6655bccea"],["/img/jpg/news-inner.jpg","13da278b204d1186929f3828dc58cb2d"],["/img/jpg/news.jpg","303baa4fb62204eece5a5a4a1ace8300"],["/img/jpg/pat.jpg","3879bc8766e53c894aa7bff880fcca04"],["/img/jpg/pug.jpg","f7a6010edf9c41ed701d58ada76aa0f2"],["/img/jpg/reh.jpg","614da61360f5a10badb8764cbfafe160"],["/img/jpg/slider1.jpg","2627f34da11d7c8be37230b657ef0516"],["/img/jpg/treatment.jpg","6ed9ac987d4b3750a69db41ba248ad0f"],["/img/jpg/treatment1.jpg","7f5aae8f0d5e3227724f745e53a7d42b"],["/img/jpg/vra4.jpg","8ccdd251e65b128914494a8bc4325168"],["/img/loading.gif","e46d34673a4d1335d99396af0cc9ff43"],["/img/png/a1.png","302dbf636eb3b3e5299b27f7ee5bf565"],["/img/png/a2.png","d93549c4ca118e011d376c2ce1191b11"],["/img/png/a3.png","9cdbea1db676ea738094955cd93d13f1"],["/img/png/ab1.png","5b611631704a6d1d410a06b10e4a3d9d"],["/img/png/ab2.png","c29b6431b9bb4f416ae8169fce7b5530"],["/img/png/ab3.png","6e9b6d5445011d89a5315b72c00474aa"],["/img/png/ad1.png","82af7a93aab2a18c14bf8c8211c5755e"],["/img/png/ad2.png","79b62bc9ea851eceac3d9fc9689dd209"],["/img/png/ad3.png","9b033692509fee0fda6732066dbe30f8"],["/img/png/beeline.png","3eaab0715a2d22b4356f91f18a97950b"],["/img/png/big-loop.png","116dbddef8be0e9e8eb1980e1b94ab61"],["/img/png/calendar.png","b4de4bc2a4ee1ca2328d914eebb7128b"],["/img/png/calendar2.png","f42e329ddcca1c59472778ccb6efc472"],["/img/png/calendar3.png","d9061ae264e8b1efa58ac9111d4a10fe"],["/img/png/coast.png","b8fcb3a8e8dd709e2a0036bb808e5f68"],["/img/png/dia1.png","0cfdb84b15d008524fcf2270744bb6c0"],["/img/png/dia2.png","e6f1e1a63ddebf3387acfdf670d64695"],["/img/png/dia3.png","235cfecb0993d2e08988a1cb4a958864"],["/img/png/doctor.png","1f57bdcdb7dccf4561c6feb8e3af8251"],["/img/png/ex.png","be58a1d23936e211567c8cee4f76a2f1"],["/img/png/l1.png","4fa32c9764c48dbe5ecfbfd08e771d5e"],["/img/png/l2.png","fc7b0c0412e544e82b89b87844b13476"],["/img/png/l3.png","ddcd81a2de07eb3b7a9aa61aa451b459"],["/img/png/l4.png","3988da255bc0fcd1d3a455552c0733db"],["/img/png/l5.png","38d649d19f0cdb984a19bb824506a5d2"],["/img/png/l6.png","61d1be434e677b45080da4d90c922c60"],["/img/png/l7.png","6c00da3a73756481f0ef20535769baad"],["/img/png/list.png","a34b0d0c09ab28d6bc8e0e264def5f5e"],["/img/png/logo.png","9925ee45a388082c94fc70f8dc289668"],["/img/png/logo2.png","5b291c216514c3ec68e3a6c7a7a36d8e"],["/img/png/loop.png","4558d6dd55309f3618f94f1af81c1a43"],["/img/png/medic.png","4c3f18b3204aed2739e638ce16efb53c"],["/img/png/megacom.png","6dbf9e3af72a460eacc98c4b4bea997c"],["/img/png/modal-h.png","a936230d24d591e370948ec6e84ea341"],["/img/png/o!.png","f8ebd55305b4107af9fd3171a771fd34"],["/img/png/qu.png","04eb37b950e23791702cc82b7351ac19"],["/img/png/reh1.png","4f2c8beada493927876b6791fb7c648b"],["/img/png/share.png","b47b74924f135b9ada9c9907dc67d8c6"],["/img/png/slider-bg.png","4299d8630933ffb67ed50d1c3986d781"],["/img/png/slider-bgs.png","6991677d5c602dc60e05452d2e1b8099"],["/img/png/time-icon.png","5457e82921362bb58ba067e4e45e2fac"],["/img/png/tr1.png","696eb90fec139f5114d03ed156d945b2"],["/img/png/tr2.png","c81c1d981b8a65e03fbf6b9b6d288046"],["/img/png/tr3.png","a7ff857f92f4b6df0eb1d7c33238eaeb"],["/img/png/treatment1.png","727c71f7f4d3bf4d5003bb2474107c83"],["/img/png/user.png","bbf9d0bab3a0807d44dd1dbf3eab6f2d"],["/index.html","3dd523eb91669fce09dcc7abf3506212"],["/js/common.min.js","5fdda4d29186bb3b04208482920fb255"],["/js/libs.min.js","338213c0f4c5991dcdbb5660357210ce"],["/manifest.json","cd97fb57f20e6b285fc5398738a312e3"],["/news-inner.html","4758854e7fd55f72120bee23bdd01b4e"],["/personal-area-check-in-step1.html","a626f6cbf8980c064960e42b37018c6e"],["/personal-area-check-in-step2.html","a438416aa67c1e9502a06aec367d6295"],["/personal-area-check-in-step3.html","34d17d48f2f123e046bb2d551464a76d"],["/personal-area-check-in-step4.html","25a602c054eec315aef1e9739d3c6324"],["/personal-area-check-in-step5.html","ef7b8efcf88ba7a6697f146832939607"],["/personal-area-my-treatment.html","63af1ac296614667424f623233ae7d01"],["/personal-area-visit-history.html","ea7f8594a2e44121ac51453a86053d3a"],["/personal-area.1.html","8249f606d6354321e255a2f12102b764"],["/personal-area.html","22be16e0f5811c73424531c2e1f8e023"],["/price-page.html","5c1d650b37175976de5b440a2c950c3b"],["/services-inner.html","1f53ce6b5b209815bb9fd7db3047f8ee"],["/services-inner2.html","d35207684a4092736b47e000cba99908"],["/services.html","88d04733f4e1b3f0d1d14974881ca91f"],["/treatment-inner.html","89aa277e157a75ac570e1753c08f55cb"],["/treatment.html","41f0eabad224f4b245736e8ef5026020"],["/we-spec.html","c2ad80f4c4f751af57cb22972735a9a6"]];
var cacheName = 'sw-precache-v3--' + (self.registration ? self.registration.scope : '');


var ignoreUrlParametersMatching = [/^utm_/];



var addDirectoryIndex = function (originalUrl, index) {
    var url = new URL(originalUrl);
    if (url.pathname.slice(-1) === '/') {
      url.pathname += index;
    }
    return url.toString();
  };

var cleanResponse = function (originalResponse) {
    // If this is not a redirected response, then we don't have to do anything.
    if (!originalResponse.redirected) {
      return Promise.resolve(originalResponse);
    }

    // Firefox 50 and below doesn't support the Response.body stream, so we may
    // need to read the entire body to memory as a Blob.
    var bodyPromise = 'body' in originalResponse ?
      Promise.resolve(originalResponse.body) :
      originalResponse.blob();

    return bodyPromise.then(function(body) {
      // new Response() is happy when passed either a stream or a Blob.
      return new Response(body, {
        headers: originalResponse.headers,
        status: originalResponse.status,
        statusText: originalResponse.statusText
      });
    });
  };

var createCacheKey = function (originalUrl, paramName, paramValue,
                           dontCacheBustUrlsMatching) {
    // Create a new URL object to avoid modifying originalUrl.
    var url = new URL(originalUrl);

    // If dontCacheBustUrlsMatching is not set, or if we don't have a match,
    // then add in the extra cache-busting URL parameter.
    if (!dontCacheBustUrlsMatching ||
        !(url.pathname.match(dontCacheBustUrlsMatching))) {
      url.search += (url.search ? '&' : '') +
        encodeURIComponent(paramName) + '=' + encodeURIComponent(paramValue);
    }

    return url.toString();
  };

var isPathWhitelisted = function (whitelist, absoluteUrlString) {
    // If the whitelist is empty, then consider all URLs to be whitelisted.
    if (whitelist.length === 0) {
      return true;
    }

    // Otherwise compare each path regex to the path of the URL passed in.
    var path = (new URL(absoluteUrlString)).pathname;
    return whitelist.some(function(whitelistedPathRegex) {
      return path.match(whitelistedPathRegex);
    });
  };

var stripIgnoredUrlParameters = function (originalUrl,
    ignoreUrlParametersMatching) {
    var url = new URL(originalUrl);
    // Remove the hash; see https://github.com/GoogleChrome/sw-precache/issues/290
    url.hash = '';

    url.search = url.search.slice(1) // Exclude initial '?'
      .split('&') // Split into an array of 'key=value' strings
      .map(function(kv) {
        return kv.split('='); // Split each 'key=value' string into a [key, value] array
      })
      .filter(function(kv) {
        return ignoreUrlParametersMatching.every(function(ignoredRegex) {
          return !ignoredRegex.test(kv[0]); // Return true iff the key doesn't match any of the regexes.
        });
      })
      .map(function(kv) {
        return kv.join('='); // Join each [key, value] array into a 'key=value' string
      })
      .join('&'); // Join the array of 'key=value' strings into a string with '&' in between each

    return url.toString();
  };


var hashParamName = '_sw-precache';
var urlsToCacheKeys = new Map(
  precacheConfig.map(function(item) {
    var relativeUrl = item[0];
    var hash = item[1];
    var absoluteUrl = new URL(relativeUrl, self.location);
    var cacheKey = createCacheKey(absoluteUrl, hashParamName, hash, false);
    return [absoluteUrl.toString(), cacheKey];
  })
);

function setOfCachedUrls(cache) {
  return cache.keys().then(function(requests) {
    return requests.map(function(request) {
      return request.url;
    });
  }).then(function(urls) {
    return new Set(urls);
  });
}

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(cacheName).then(function(cache) {
      return setOfCachedUrls(cache).then(function(cachedUrls) {
        return Promise.all(
          Array.from(urlsToCacheKeys.values()).map(function(cacheKey) {
            // If we don't have a key matching url in the cache already, add it.
            if (!cachedUrls.has(cacheKey)) {
              var request = new Request(cacheKey, {credentials: 'same-origin'});
              return fetch(request).then(function(response) {
                // Bail out of installation unless we get back a 200 OK for
                // every request.
                if (!response.ok) {
                  throw new Error('Request for ' + cacheKey + ' returned a ' +
                    'response with status ' + response.status);
                }

                return cleanResponse(response).then(function(responseToCache) {
                  return cache.put(cacheKey, responseToCache);
                });
              });
            }
          })
        );
      });
    }).then(function() {
      
      // Force the SW to transition from installing -> active state
      return self.skipWaiting();
      
    })
  );
});

self.addEventListener('activate', function(event) {
  var setOfExpectedUrls = new Set(urlsToCacheKeys.values());

  event.waitUntil(
    caches.open(cacheName).then(function(cache) {
      return cache.keys().then(function(existingRequests) {
        return Promise.all(
          existingRequests.map(function(existingRequest) {
            if (!setOfExpectedUrls.has(existingRequest.url)) {
              return cache.delete(existingRequest);
            }
          })
        );
      });
    }).then(function() {
      
      return self.clients.claim();
      
    })
  );
});


self.addEventListener('fetch', function(event) {
  if (event.request.method === 'GET') {
    // Should we call event.respondWith() inside this fetch event handler?
    // This needs to be determined synchronously, which will give other fetch
    // handlers a chance to handle the request if need be.
    var shouldRespond;

    // First, remove all the ignored parameters and hash fragment, and see if we
    // have that URL in our cache. If so, great! shouldRespond will be true.
    var url = stripIgnoredUrlParameters(event.request.url, ignoreUrlParametersMatching);
    shouldRespond = urlsToCacheKeys.has(url);

    // If shouldRespond is false, check again, this time with 'index.html'
    // (or whatever the directoryIndex option is set to) at the end.
    var directoryIndex = 'index.html';
    if (!shouldRespond && directoryIndex) {
      url = addDirectoryIndex(url, directoryIndex);
      shouldRespond = urlsToCacheKeys.has(url);
    }

    // If shouldRespond is still false, check to see if this is a navigation
    // request, and if so, whether the URL matches navigateFallbackWhitelist.
    var navigateFallback = '';
    if (!shouldRespond &&
        navigateFallback &&
        (event.request.mode === 'navigate') &&
        isPathWhitelisted([], event.request.url)) {
      url = new URL(navigateFallback, self.location).toString();
      shouldRespond = urlsToCacheKeys.has(url);
    }

    // If shouldRespond was set to true at any point, then call
    // event.respondWith(), using the appropriate cache key.
    if (shouldRespond) {
      event.respondWith(
        caches.open(cacheName).then(function(cache) {
          return cache.match(urlsToCacheKeys.get(url)).then(function(response) {
            if (response) {
              return response;
            }
            throw Error('The cached response that was expected is missing.');
          });
        }).catch(function(e) {
          // Fall back to just fetch()ing the request if some unexpected error
          // prevented the cached response from being valid.
          console.warn('Couldn\'t serve response for "%s" from cache: %O', event.request.url, e);
          return fetch(event.request);
        })
      );
    }
  }
});







