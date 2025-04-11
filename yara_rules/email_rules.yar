rule MaliciousEmail
{
    strings:
        $phish = "reset your password now"
        $exec = "cmd.exe"
        $mal_url = "http://badguy.com"

    condition:
        any of them
}
