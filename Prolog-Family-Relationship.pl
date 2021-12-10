% Shovon Roy
% 19-40023-1

parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).
male(tom).
male(bob).
male(jim).
female(pam).
female(liz).
female(ann).
female(pat).
	
grandparent(X,Z) :- parent(X,Y), parent(Y,Z).

offspring(Y,X) :- parent(X,Y).

sister(X,Y) :- parent(Z,X), parent(Z,Y), female(X).

mother(X,Y) :- parent(X,Y), female(X).   
		
aunt(X,Y) :- sister(X,A), parent(A,Y).

