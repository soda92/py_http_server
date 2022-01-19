// #define CPPHTTPLIB_OPENSSL_SUPPORT
#include "httplib.h"
#include <cstdio>
int main()
{

    // HTTP
    httplib::Client cli("http://localhost:8080");


    auto res = cli.Get("/size");
    printf("%d %s\n", res->status, res->body.c_str());
    return 0;
}