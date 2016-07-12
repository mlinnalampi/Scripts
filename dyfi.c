#include <curl/curl.h>


int main(void){
CURL *curl = curl_easy_init();
if(curl) {
  CURLcode res;

//Set the hostname to your needs

  curl_easy_setopt(curl, CURLOPT_URL, "https://www.dy.fi/nic/update?hostname=hostname.dy.fi");
//Username
  curl_easy_setopt(curl, CURLOPT_USERNAME, "email@email.com");
//Passwd
  curl_easy_setopt(curl, CURLOPT_PASSWORD, "Passwd");
  res = curl_easy_perform(curl);
  curl_easy_cleanup(curl);
}
}