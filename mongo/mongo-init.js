db.createUser({
    user: 'admin',
    pwd: 'easydata',
    roles: [
      {
        role: 'dbOwner',
        db: 'CNC',
      },
    ],
  });