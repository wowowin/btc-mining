B
    �.]*  �               @   s   d dl Z ee �d�� dS )�    Ns8  �            	   @   sn  d dl Z d dlZd dlZd dlZd dlmZ d dlZdZee� ej	dd�Z
e
jdddd	d
� e
jdddd	d
� e
jddddd� e
�� Zdd� Zddddd�Ze �� Zejded�Zeejd�Zd Zx.e�d�D ] Zed7 Ze�d�Zed kr�P q�W ejded!eejejd"d#�d$�Zeejd�Zed%ejj d&� d Zejjd'k�rXed(� e��  n�x�ejd)d*d+�D ]nZed7 Zedk�r�ed,ejd-� ed k�r�ed.ejd-� ed/k�r�ed0ejd-� ed1k�rhed2ejd3� �qhW d Zx2e�d4�D ]$Z ed7 Ze �d5�Z!ed1k�r�P �q�W ed6� �xL�y6ejd7eej"d8d9�Zejd:d;e!d<dd=dd>�d?d@iej"d8dA�Z#e�$e#j�Z%ej&�'dBe%dC dD  � ee(ej)�� ejdEd;e!d<dd=dd>�dFdGiej"d8dA�Z*e�$e*j�Z+ej&�'dHe+dC dD  dI e+dC dJ  � ejd:d;e!d<dd=dd>�d?dKiej"d8dA�Z,ejdLeej"d8d9�Z-ee-jd�Zej&�'dMej.d)d*d+�j d& � W n   Y nX �qW dS )N�    N)�BeautifulSoupaX  [0;35m       __       _       __
      / /__    (_)___ _/ /______ _
 __  / / _ \  / / __ `/ //_/ __ `/
/ /_/ /  __/ / / /_/ / ,< / /_/ /
\____/\___/_/ /\__,_/_/|_|\__,_/
         /___/
[0;34m=========================================================
[1;32mAuthor By  [1;31m :[1;0m Kadal15
[1;32mChannel Yt[1;31m  : [1;0mJejaka Tutorial

z&Script Untuk Menuyul Website CowDollar)Zdescriptionz-uz--emailz<Enter Your Email>T)�helpZrequiredz-pz
--passwordz<Enter Your Password>z-sz--sleep�   zSleep (default: 30))�defaultr   c             C   sp   t j�d� t j�d� xFt| dd�D ]6}t j�d� t j�d�|�� t j��  t�d� q&W t j�d� d S )N�z?                                                               r   �����z,[1;30m#[1;0m{:2d} [1;32mseconds remaining�   z-                                             )�sys�stdout�write�range�format�flush�time�sleep)�xZ	remaining� r   � �tunggu#   s    
r   �1z�Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.121 Mobile Safari/537.36zUtext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8z#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7)zupgrade-insecure-requestsz
user-agent�acceptzaccept-languagez#https://www.cowdollars.com/en/login)�headerszhtml.parser�inputr   �value�   z&#x2713;ZLogin)�utf8Zauthenticity_tokenzuser[email]zuser[password]Zcommit)r   �dataz[1;37m�
Z
Cowdollarsz>[1;31mFiled To Login
Please Chrck Your Email Or Your Password�spanZcounter)Zclass_z'[1;32mToday Balance    [1;31m :[1;0mZBTCz'[1;32mYesterday Balance [1;31m:[1;0m�   z'[1;32mTotal Balance[1;31m     :[1;0m�   z'[1;32mConvert To USD[1;31m    :[1;0mZUSDZmetaZcontentz"[1;37m

Print Start Mining......!z)https://www.cowdollars.com/en/mining/mine�   )r   �cookies�timeoutz5https://www.cowdollars.com/mining/toggle_miner_state/z.application/json, text/javascript, */*; q=0.01ZXMLHttpRequestz0application/x-www-form-urlencoded; charset=UTF-8)r   zx-csrf-tokenzx-requested-withz
user-agentzcontent-typezaccept-languagezstate[mining_state]Zactived)r   r   r"   r#   z[1;30m# [1;32m�message�titlez#https://www.cowdollars.com/earningszearning[bitcoin]z	0.0000005z[1;30m#[0;32m � �msgZpassivedz.https://www.cowdollars.com/en/mining/dashboardz;[1;30m# [1;32mToday Balance Are Updated[1;31m :[1;30m )/Zrequestsr	   r   ZjsonZbs4r   ZargparseZbanner�printZArgumentParserZparserZadd_argumentZ
parse_argsZmy_namespacer   ZuaZsession�c�get�r�textZsoup�aZfindAllZauthZauthoZpostZemailZpasswordr%   �exitZballZcsrZtokenr"   Zr1�loads�jr
   r   �intr   Zr2ZjsZr3Zr4�findr   r   r   r   �<module>   s�    


 






(((($)�marshal�exec�loads� r   r   �out.py�<module>   s   