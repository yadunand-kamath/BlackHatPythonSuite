#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>

#include "console.hpp"

#ifdef _WIN32
    #include <windows.h>
    #include <conio.h>
#elif defined(__linux__)
    #include <unistd.h>
    #include <termios.h>
#endif

struct PythonScript
{
    std::string name;
    std::string description;
    std::string path;
};

const std::vector<PythonScript> scripts = {
    {"ARP Spoofer", "", "python_scripts/arp_spoofer.py"},
    {"ARP Spoof Detector", "", "python_scripts/arp_spoof_detector.py"},
    {"Bruteforce Login", "", "python_scripts/login_bruteforcer.py"}, 
    {"Bruteforce SSH", "", "python_scripts/threaded_ssh_bruteforcer.py"},
    {"Code Injector", "", "python_scripts/code_injector.py"},
    {"DNS Spoofer", "", "python_scripts/dns_spoofer.py"},
    {"Email Scraper", "", "python_scripts/email_scraper.py"},
    {"File Interceptor", "", "python_scripts/file_interceptor.py"},
    {"Key Logger", "", "python_scripts/key_logger.py"},
    {"MAC Address Changer", "", "python_scripts/mac_changer.py"},
    {"Mail Phishing", "", "python_scripts/mail_phishing.py"},
    {"Network Scanner", "", "python_scripts/network_scanner.py"},
    {"Packet Sniffer", "", "python_scripts/packet_sniffer.py"},
    {"Password Hash Cracker", "", "python_scripts/password_hash_cracker.py"},
    {"Password Sniffer", "", "python_scripts/password_sniffer.py"},
    {"Port Scanner", "", "python_scripts/port_scanner.py"},
    {"Vulnerability Scanner", "", "python_scripts/vulnerability_scanner.py"},
    {"Website Crawler", "", "python_scripts/website_crawler.py"}
};

void menu()
{
    std::cout << "0. Exit\n";
    for(int i = 0; i < scripts.size(); i++)
    {
        std::cout << i + 1 <<  ". " << scripts[i].name << " - " << 
          scripts[i].description << std::endl;
    }
    std::cout << "Enter option:\n";
}

void read()
{
    int choice;
    std::cin >> choice;

    switch(choice)
    {
        case 0:
            std::cout << "Exiting..." << std::endl;
            break;
        # TODO: Add other options
        default:
            std::cout << "-xx-Invalid Option-xx-" << std::endl;
    }
}

int main()
{
    console::clear();
    menu();
    read();
    return 0;
}

