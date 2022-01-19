// #define CPPHTTPLIB_OPENSSL_SUPPORT
#include "httplib.h"
#include <cstdio>
#include <boost/json/src.hpp>
using namespace boost::json;

int main()
{

    // HTTP
    httplib::Client cli("http://localhost:8080");
    auto res = cli.Get("/size");
    printf("%d %s\n", res->status, res->body.c_str());
    value jv = parse(res->body);
    auto total = jv.at("total").as_double();
    auto used = jv.at("used").as_double();
    auto free = jv.at("free").as_double();
    printf("total: %lf, used: %lf, free: %lf\n", total, used, free);
    return 0;
}