with open('index.html', 'r') as f:
    html = f.read()

parts = html.split('<!-- Boarding Pass Ticket -->')
if len(parts) == 2:
    before = parts[0]
    ticket = parts[1]
    
    # Also separate the ticket from the footer just in case
    ticket_parts = ticket.split('<!-- Footer -->')
    if len(ticket_parts) == 2:
        ticket = ticket_parts[0]
        after = '<!-- Footer -->' + ticket_parts[1]
        
        ticket = ticket.replace('text-white/40', 'text-gray-400')
        ticket = ticket.replace('bg-transparent text-white', 'bg-olive text-white') # VIP Guest button
        
        html = before + '<!-- Boarding Pass Ticket -->' + ticket + after

with open('index.html', 'w') as f:
    f.write(html)
