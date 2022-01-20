// #define CPPHTTPLIB_OPENSSL_SUPPORT
#include "httplib.h"
#include <cstdio>
#include <boost/json/src.hpp>
#include <thread>
#include <chrono>
using namespace boost::json;
using namespace std;

int main()
{
    // HTTP
    httplib::Client cli("http://localhost:55555");
    auto res = cli.Get("/hide");
    this_thread::sleep_for(10s);
    res = cli.Get("/show");
    return 0;
}
