import time
import os
if os.name == "nt":
    os.system("pip install -r requirements.txt")
else:
    try:
        os.system("apt install python3-pip")
        from pip._internal.utils.misc import get_installed_distributions 
        os.system("pip install -r requirements.txt")
        os.system("pip3 install -r requirements.txt")
    except:
        try:
            os.system("yum install epel-release")
            os.system("yum install python-pip")
            from pip._internal.utils.misc import get_installed_distributions
            os.system("pip install -r requirements.txt")
            os.system("pip3 install -r requirements.txt")
        except:
            try:
                os.system("dnf install python3")
                from pip._internal.utils.misc import get_installed_distributions
                os.system("pip install -r requirements.txt")
                os.system("pip3 install -r requirements.txt")
            except:
                try:
                    os.system("pacman -S python-pip")
                    from pip._internal.utils.misc import get_installed_distributions
                    os.system("pip install -r requirements.txt")
                    os.system("pip3 install -r requirements.txt")
                except:
                    try:
                        os.system("zypper install python3-pip")
                        from pip._internal.utils.misc import get_installed_distributions
                        os.system("pip install -r requirements.txt")
                        os.system("pip3 install -r requirements.txt")
                    except:
                        pass
time.sleep(1)
