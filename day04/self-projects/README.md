# CLI Contact Book — Project Overview & Roadmap
Built using only: variables, strings, lists, dictionaries, 
conditionals, loops, and input/output. No functions, no try/except, 
no classes yet — every design choice below reflects that constraint, 
on purpose.
- Add New Contact -- Prompts for name, phone, email; re-prompts on empty input; 
  appends a dict to contact_list
- View Contact List -- Lists all contacts numbered by position (SNO); 
  shows a friendly message if the list is empty
- Edit/Update Existing Contact -- Looks up a contact by SNO, 
  lets you update name, phone, email, or all three.
- Delete Contact -- Looks up a contact by SNO, shows it, 
  asks for Y/N confirmation before removing it.
- Quit -- Exits the while True loop cleanly

# Features for Enhancement
- Duplicate detection — loop through contact_list before adding and 
  warn if the name or phone already exists.
- Search by name or phone — a new menu option that loops through 
  contact_list and prints matches, instead of only supporting lookup 
  by SNO.
- Basic email sanity check — reject anything without an "@" before 
  accepting it.
- Simplify the menu validation — if choice not in {"1","2","3","4","5"}: 
  replaces the two-step isdigit() + range check with one line.
